package com.demo.controller;

import com.demo.Service.ChinaPeopleService;
import com.demo.Service.WorldService;
import com.demo.entity.ChinaPeople;
import com.demo.entity.World;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@CrossOrigin
@RestController
@RequestMapping("/chinaPeople")
public class ChinaPeopleController {
    @Autowired
    ChinaPeopleService chinaPeopleService;
    @GetMapping("findChinaPeople")
    public Map<String,Object> getAllChinaPeople(String page, String rows){
        Map<String, Object> map=new HashMap<>();
        List<ChinaPeople> results=chinaPeopleService.findAll();

        map.put("total",1);
        map.put("totalPage",1);
        map.put("page",page);
        map.put("results",results);
        return map;
    }
}
