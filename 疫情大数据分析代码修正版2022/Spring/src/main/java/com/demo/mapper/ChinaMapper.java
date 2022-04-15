package com.demo.mapper;


import com.demo.entity.China;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper

public interface ChinaMapper {
    List<China> findAll();
    List<China> findXianggang();
    List<China> findNow();
    String findToday();
    List<China> findYesterday();
}