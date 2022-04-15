package com.demo.controller;

import com.demo.Service.WorldService;
import com.demo.entity.Student;
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
@RequestMapping("/world")

public class WorldController {
    @Autowired
    WorldService worldService;
    @GetMapping("findAllWorld")
    public Map<String,Object> getAllWorld(){
        Map<String, Object> map=new HashMap<>();
        List<World> results=worldService.findAll();

        map.put("results",results);
        return map;
    }
}
