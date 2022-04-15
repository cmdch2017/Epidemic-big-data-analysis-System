package com.demo.Service;



import com.demo.entity.Student;
import org.springframework.stereotype.Service;

import java.util.List;

public interface StudentService {

    void addStudent(Student student);

    void updateStudent(Student student);

    void deleteStudent(Student student);

    List<Student> findAll();

    Student findById(String id);
}
