package com.demo.controller;

import com.demo.Service.ChinaService;
import com.demo.entity.China;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@CrossOrigin
@RestController
@RequestMapping("/china")

public class ChinaController {
    @Autowired
    ChinaService chinaService;
    @PostMapping("DataAdd")
    public Map<String,Object> addData(){
        //现场爬取数据
        String[] arguments = new String[] {"python3", "/root/Epidemic_Data/20210520.py"};
        now(arguments);
        HashMap<String,Object> map=new HashMap<>();
        List<China> results;
        if(chinaService.findToday().equals("0")) {
             results = chinaService.findYesterday();
        }else{
             results = chinaService.findNow();
        }
        try {
            map.put("results",results);
            map.put("success",true);
            map.put("msg","添加成功");
        } catch (Exception e) {
            e.printStackTrace();
            map.put("success",false);
            map.put("msg","添加失败");
        }
        return map;
    }

    public static void now(String[] arguments) {
        try {
            Process process = Runtime.getRuntime().exec(arguments);
            BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream(),
                    "GBK"));
            String line = null;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }
            in.close();
            //java代码中的process.waitFor()返回值为0表示我们调用python脚本成功，
            //返回值为1表示调用python脚本失败，这和我们通常意义上见到的0与1定义正好相反
            int re = process.waitFor();
            System.out.println(re);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @GetMapping("findAllChina")
    public Map<String, Object> getAllWorld() {
        Map<String, Object> map = new HashMap<>();
        List<China> results = chinaService.findAll();

        map.put("results", results);
        return map;
    }
    @GetMapping("findXianggang")
    public Map<String, Object> getAllXianggang() {
        Map<String, Object> map = new HashMap<>();
        List<China> results = chinaService.findXianggang();

        map.put("results", results);
        return map;
    }
}
