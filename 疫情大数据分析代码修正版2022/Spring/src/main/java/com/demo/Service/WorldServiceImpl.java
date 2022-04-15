package com.demo.Service;



import com.demo.entity.Student;
import com.demo.entity.World;
import com.demo.mapper.StudentMapper;
import com.demo.mapper.WorldMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;


@Service
@Transactional
public class WorldServiceImpl implements WorldService {

    @Autowired
    private WorldMapper worldMapper;


    @Override
    public List<World> findAll() {
        return worldMapper.findAll();
    }

}

