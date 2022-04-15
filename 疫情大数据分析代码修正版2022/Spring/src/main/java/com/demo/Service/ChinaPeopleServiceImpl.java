package com.demo.Service;

import com.demo.entity.ChinaPeople;
import com.demo.mapper.ChinaPeopleMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional
public class ChinaPeopleServiceImpl implements ChinaPeopleService{
    @Autowired
    ChinaPeopleMapper chinaPeopleMapper;
    @Override
    public List<ChinaPeople> findAll() {
        return chinaPeopleMapper.findAll();
    }
}
