package com.demo.Service;




import com.demo.entity.China;

import java.util.List;

public interface ChinaService {

     List<China> findAll();
     List<China> findXianggang();
     List<China> findNow();
     String findToday();
     List<China> findYesterday();

}
