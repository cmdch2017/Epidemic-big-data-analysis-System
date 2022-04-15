package com.demo.controller;

import com.demo.Service.StudentService;
import com.demo.entity.Student;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@CrossOrigin
@RestController
@RequestMapping("/student")
public class StudentController {

    @Autowired
    StudentService studentService;

    @RequestMapping("t1")
    public String test(){
        return "text";
    }
    @GetMapping("findAll")
    public Map<String,Object> getAllStudent(String page,String rows){
        Map<String, Object> map=new HashMap<>();
        List<Student> results=studentService.findAll();

        map.put("total",1);
        map.put("totalPage",1);
        map.put("page",page);
        map.put("results",results);
        return map;
    }


    @PostMapping("add")
    public Map<String,Object> addStudent(@RequestBody Student student){
        HashMap<String,Object> map=new HashMap<>();
        studentService.addStudent(student);
        try {
            map.put("success",true);
            map.put("msg","添加成功");
        } catch (Exception e) {
            e.printStackTrace();
            map.put("success",false);
            map.put("msg","添加失败");
        }
        return map;
    }

    @GetMapping("findOne")
    public Student findById(String id){
        return studentService.findById(id);
    }
    @PostMapping("update")
    public Map<String,Object> updateStudent(@RequestBody Student student){
        HashMap<String,Object> map=new HashMap<>();
        studentService.updateStudent(student);
        try {
            map.put("success",true);
            map.put("msg","更新学生信息成功");
        } catch (Exception e) {
            e.printStackTrace();
            map.put("success",false);
            map.put("msg","更新学生信息失败");
        }
        return map;
    }
    @GetMapping("delete")
    public Map<String,Object> deleteStudent(Student student){
        HashMap<String,Object> map=new HashMap<>();
        studentService.deleteStudent(student);
        try {
            map.put("success",true);
            map.put("msg","删除成功");
        } catch (Exception e) {
            e.printStackTrace();
            map.put("success",false);
            map.put("msg","删除失败");
        }
        return map;
    }
}
