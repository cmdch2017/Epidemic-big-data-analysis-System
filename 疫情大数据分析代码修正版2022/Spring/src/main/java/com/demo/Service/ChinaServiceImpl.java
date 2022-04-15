package com.demo.Service;



import com.demo.entity.China;
import com.demo.mapper.ChinaMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;


@Service
@Transactional
public class ChinaServiceImpl implements ChinaService {

    @Autowired
    private ChinaMapper chinaMapper;


    @Override
    public List<China> findAll() {
        return chinaMapper.findAll();
    }

    @Override
    public List<China> findXianggang() {
        return chinaMapper.findXianggang();
    }
    @Override
    public List<China> findNow() {
        return chinaMapper.findNow();
    }

    @Override
    public String findToday() {
        return chinaMapper.findToday();
    }

    @Override
    public List<China> findYesterday() {
        return chinaMapper.findYesterday();
    }
}

