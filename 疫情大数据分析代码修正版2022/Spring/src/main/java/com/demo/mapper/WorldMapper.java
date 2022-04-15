package com.demo.mapper;


import com.demo.entity.World;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper

public interface WorldMapper {
    List<World> findAll();
}