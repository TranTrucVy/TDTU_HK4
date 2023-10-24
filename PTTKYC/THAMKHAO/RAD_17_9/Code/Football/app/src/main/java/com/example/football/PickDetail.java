package com.example.football;

import androidx.room.ColumnInfo;
import androidx.room.Entity;
import androidx.room.PrimaryKey;

import java.io.Serializable;

@Entity(tableName = "detail")
public class PickDetail implements Serializable {
    @PrimaryKey(autoGenerate = true)
    int id = 0;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    @ColumnInfo(name = "field_name")
    String field_name = "";

    public String getField_name() {
        return field_name;
    }

    public void setField_name(String field_name) {
        this.field_name = field_name;
    }

    @ColumnInfo(name = "field_type")
    String field_type = "";

    public String getField_type() {
        return field_type;
    }

    public void setField_type(String field_type) {
        this.field_type = field_type;
    }

    @ColumnInfo(name = "client")
    String client = "";

    public String getClient() {
        return client;
    }

    public void setClient(String client) {
        this.client = client;
    }

    @ColumnInfo(name = "user_mail")
    String user_mail = "";

    public String getUser_mail() {
        return user_mail;
    }

    public void setUser_mail(String user_mail) {
        this.user_mail = user_mail;
    }

    @ColumnInfo(name = "phone_num_client")
    String phone_num_client = "";

    public String getPhone_num_client() {
        return phone_num_client;
    }

    public void setPhone_num_client(String phone_num_client) {
        this.phone_num_client = phone_num_client;
    }

    @ColumnInfo(name = "date_order")
    String date_order = "";

    @ColumnInfo(name = "price")
    String price = "";

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public String getDate_order() {
        return date_order;
    }

    public void setDate_order(String date_order) {
        this.date_order = date_order;
    }

    @ColumnInfo(name = "time_frame_1")
    boolean time_frame_1 = false;

    @ColumnInfo(name = "time_frame_2")
    boolean time_frame_2 = false;

    @ColumnInfo(name = "time_frame_3")
    boolean time_frame_3 = false;

    @ColumnInfo(name = "time_frame_4")
    boolean time_frame_4 = false;

    public boolean isTime_frame_1() {
        return time_frame_1;
    }

    public void setTime_frame_1(boolean time_frame_1) {
        this.time_frame_1 = time_frame_1;
    }

    public boolean isTime_frame_2() {
        return time_frame_2;
    }

    public void setTime_frame_2(boolean time_frame_2) {
        this.time_frame_2 = time_frame_2;
    }

    public boolean isTime_frame_3() {
        return time_frame_3;
    }

    public void setTime_frame_3(boolean time_frame_3) {
        this.time_frame_3 = time_frame_3;
    }

    public boolean isTime_frame_4() {
        return time_frame_4;
    }

    public void setTime_frame_4(boolean time_frame_4) {
        this.time_frame_4 = time_frame_4;
    }
}
