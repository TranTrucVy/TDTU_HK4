package com.example.football;

import static androidx.room.OnConflictStrategy.REPLACE;

import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.Query;

import java.util.List;

@Dao
public interface FieldDAO {
    @Insert(onConflict = REPLACE)
    void insert(FieldFB field);

    @Query("SELECT * FROM field ORDER BY id ASC")
    List<FieldFB> getAll();

    @Query("SELECT * FROM field WHERE id = :id")
    FieldFB getFieldById(int id);

    @Query("SELECT COUNT(id) FROM field")
    int getSize();

    @Delete
    void delete(FieldFB field);
}
