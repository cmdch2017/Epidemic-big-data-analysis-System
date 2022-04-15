package com.demo.entity;

import lombok.AllArgsConstructor;
import lombok.experimental.Accessors;

@AllArgsConstructor
@Accessors(chain = true)
public class World {
    String world_name;
    String world_confirm;
    String world_heal;
    String world_dead;
    String world_date;

    public String getWorld_name() {
        return world_name;
    }

    public void setWorld_name(String world_name) {
        this.world_name = world_name;
    }

    public String getWorld_confirm() {
        return world_confirm;
    }

    public void setWorld_confirm(String world_confirm) {
        this.world_confirm = world_confirm;
    }

    public String getWorld_heal() {
        return world_heal;
    }

    public void setWorld_heal(String world_heal) {
        this.world_heal = world_heal;
    }

    public String getWorld_dead() {
        return world_dead;
    }

    public void setWorld_dead(String world_dead) {
        this.world_dead = world_dead;
    }

    public String getWorld_date() {
        return world_date;
    }

    public void setWorld_date(String world_date) {
        this.world_date = world_date;
    }
}
