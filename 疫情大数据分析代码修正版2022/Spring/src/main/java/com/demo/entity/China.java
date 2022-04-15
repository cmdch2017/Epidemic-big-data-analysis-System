package com.demo.entity;

import lombok.AllArgsConstructor;
import lombok.experimental.Accessors;

@AllArgsConstructor
@Accessors(chain = true)
public class China {
    String name;
    String confirm;
    String confirm_all;
    String dead;
    String heal;
    String last_update_time;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getConfirm() {
        return confirm;
    }

    public void setConfirm(String confirm) {
        this.confirm = confirm;
    }

    public String getConfirm_all() {
        return confirm_all;
    }

    public void setConfirm_all(String confirm_all) {
        this.confirm_all = confirm_all;
    }

    public String getDead() {
        return dead;
    }

    public void setDead(String dead) {
        this.dead = dead;
    }

    public String getHeal() {
        return heal;
    }

    public void setHeal(String heal) {
        this.heal = heal;
    }

    public String getLast_update_time() {
        return last_update_time;
    }

    public void setLast_update_time(String last_update_time) {
        this.last_update_time = last_update_time;
    }
}
