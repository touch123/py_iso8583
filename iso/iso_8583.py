#! /usr/bin/env python
# -*- coding: utf-8 -*

import cfg_8583
import deal_8583
import hexdump
import re

class iso_8583:
    __8583_cfg=None
    __8583_str=""
    __8583_dic={}
    
    offset = 0
    bitmap = None
    
    __deal_content_type_funcs=None
    __deal_len_type_funcs=None
    
    def __init__(self, iso_conf = None,iso_str = None):
        
        #tips:iso_conf为空，或者配置错误，劳资都是木有办法玩的。
        assert iso_conf != None,"iso_conf can not None"
        assert len(cfg_8583.ContentTypes) > 0 , "cfg_8583 err "  
        assert cfg_8583.ContentTypes.has_key(iso_conf),"iso_conf not in cfg_8583"  
            
        self.__deal_content_type_funcs=deal_8583.deal_content_type()
        self.__deal_len_type_funcs=deal_8583.deal_len_type()
        self.__8583_cfg = cfg_8583.ContentTypes[iso_conf]
        
        if iso_str != None:
            #unpack
            self.__8583_str = iso_str
            
    def __get_info(self,domain):
        cfg_domain=self.__8583_cfg[domain]
        
        len_func_name="%s_unpack" % cfg_domain["len_type"]
        len_func = getattr(self.__deal_len_type_funcs, len_func_name)
        content_type_func_name="%s_unpack" % cfg_domain["content_type"]
        content_type_func = getattr(self.__deal_content_type_funcs, content_type_func_name)
        
        len,offset_len=len_func(cfg_domain,self.__8583_str,self.offset)  
        self.offset += offset_len
        
        val,offset_data=content_type_func(self.__8583_str,len,self.offset)  
        self.offset += offset_data
        
        return (domain,val)
    
    def __gen_info(self,domain):
        if self.__8583_cfg.has_key(domain) :
            cfg_domain=self.__8583_cfg[domain]
            data = self.__8583_dic[domain]
            
            len_func_name="%s_pack" % cfg_domain["len_type"]
            len_func = getattr(self.__deal_len_type_funcs, len_func_name)
            content_type_func_name="%s_pack" % cfg_domain["content_type"]
            content_type_func = getattr(self.__deal_content_type_funcs, content_type_func_name)
            
            
            info={}
            info["len"]=len_func(cfg_domain,data)
            info["val"]=content_type_func(data)  
            
            return info["len"] + info["val"]
        else:
            return ""
        
    def __gen_bitmap_list(self):
        bitmap_list = []
        index=1
        for x in self.bitmap:
            b="%4s" % bin(int(x,16))[2:]
            j=0
            for y in b:
                if y == '1':
                    bitmap_list.append(index+j)
                j+=1
             
            index+=4
        return bitmap_list
    
    def __gen_bitmap(self):
        bitmap_list = [key for key in self.__8583_dic if key >= 1]
        
        bitmap="0"*64
        for x in bitmap_list:
            if x >=1 :
                bitmap="%s1%s" % (bitmap[:x-1],bitmap[x:])
        tmp = re.findall(r'.{4}',bitmap)
        self.bitmap = ''.join([hex(int(c,2))[2:].upper() for c in tmp])
        return self.bitmap
        #print self.bitmap
    
    def unpack(self):
        for domain in range(-6,0):
            if self.__8583_cfg.has_key(domain):
                t, v = self.__get_info(domain)
                self.__8583_dic[t] = v
            
        self.bitmap = self.__8583_dic[-2]
        bitmap_list = self.__gen_bitmap_list()
        print "get bitmap list succ %s" % bitmap_list
        
        for domain in bitmap_list:
            if self.__8583_cfg.has_key(domain):
                t, v = self.__get_info(domain)
                self.__8583_dic[t] = v
        
        return self.__8583_dic
    
    def set_bit(self,t,v):
        self.__8583_dic[t] = v
    
    def pack(self):
        self.__8583_str=""
                
        self.__8583_dic[-2]={}
        self.__8583_dic[-2]=self.__gen_bitmap()
                
        body_list = []
        pack_list = [key for key in self.__8583_dic if key >= -5]
        pack_list.sort()
        for d in pack_list:
            body_list.append(self.__gen_info(d))
        
        body = "".join(body_list)
        body_len = len(body)
        ret = "%s%s" % ("%04X" % (body_len/2),body)
        return ret
                
            
    def ISO8583_testOutput(self):  
        for d in range(-6,128+1):
            if self.__8583_dic.has_key(d):
                print "[%2s] [%08s] [%08s] [%03s] : %s" % \
                (
                 d,
                 self.__8583_cfg[d]["content_type"],
                 self.__8583_cfg[d]["len_type"],
                 self.__8583_cfg[d]["max_len"],
                 self.__8583_dic[d]
                 )
            