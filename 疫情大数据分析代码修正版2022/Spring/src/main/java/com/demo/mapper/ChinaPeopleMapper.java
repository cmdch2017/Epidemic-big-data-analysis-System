package com.demo.mapper;

import com.demo.entity.ChinaPeople;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface ChinaPeopleMapper {
    List<ChinaPeople> findAll();

}
