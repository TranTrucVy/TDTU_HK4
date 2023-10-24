package com.example.football;

import static androidx.room.OnConflictStrategy.REPLACE;

import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.Query;

import java.util.List;

@Dao
public interface DetailDAO {
    @Insert(onConflict = REPLACE)
    void insert(PickDetail detail);

    @Query("SELECT * FROM detail ORDER BY id ASC")
    List<PickDetail> getAll();

    @Query("SELECT * FROM detail WHERE user_mail = :user ORDER BY id DESC")
    List<PickDetail> getAllForUser(String user);

    @Query("SELECT * FROM detail WHERE field_name = :nameField AND date_order = :date AND price = :price")
    List<PickDetail> getAllForCheckInsert(String nameField, String date, String price);

    @Query("SELECT * FROM detail WHERE id = :id")
    PickDetail getDetailById(int id);

    @Query("SELECT COUNT(id) FROM detail")
    int getSize();

    @Query("SELECT * FROM detail WHERE field_name = :name AND date_order = :date")
    List<PickDetail> getAllOrderByDateAndName(String name, String date);

    @Query("UPDATE detail SET date_order = :date WHERE id = :id")
    void updateDateOrder(int id, String date);

    @Delete
    void delete(PickDetail detail);
}
