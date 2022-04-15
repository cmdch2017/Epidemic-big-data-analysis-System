package com.demo;

import com.demo.controller.ChinaController;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class JavaPythonFile {
    public static void main(String[] args) {
        String[] arguments = new String[] {"python", "C:\\Users\\67099\\PycharmProjects\\pythonProject\\20210520.py"};
        ChinaController.now(arguments);
    }
}