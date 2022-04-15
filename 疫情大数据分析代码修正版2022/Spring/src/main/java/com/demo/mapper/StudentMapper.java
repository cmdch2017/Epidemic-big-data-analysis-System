package com.demo.mapper;


import org.apache.ibatis.annotations.Mapper;
import com.demo.entity.Student;

import java.util.List;
@Mapper

public interface StudentMapper {

    void addStudent(Student student);

    void updateStudent(Student student);

    void deleteStudent(Student student);

    List<Student> findAll();

    Student findById(String id);
}
