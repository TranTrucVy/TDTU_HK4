package com.example.football;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.google.firebase.auth.FirebaseAuth;

import java.util.ArrayList;
import java.util.List;

public class HistoryPickActivity extends AppCompatActivity {

    RecyclerView rView;
    ImageView back_main;
    TextView notify_empty;
    HistoryAdapter hAdapter;
    List<PickDetail> lDetails = new ArrayList<>();
    LinearLayout table_zone;
    FirebaseAuth user = FirebaseAuth.getInstance();
    RoomDB db = RoomDB.getInstance(this);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_history_pick);

        rView = findViewById(R.id.rView);
        table_zone = findViewById(R.id.table_zone);
        notify_empty = findViewById(R.id.notify_empty);
        back_main = findViewById(R.id.back_main);

        back_main.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });

        lDetails.clear();
        lDetails.addAll(db.detailDAO().getAllForUser(user.getCurrentUser().getEmail()));

        hAdapter = new HistoryAdapter(HistoryPickActivity.this, lDetails);

        LinearLayoutManager manager = new LinearLayoutManager(HistoryPickActivity.this,
                LinearLayoutManager.VERTICAL,false);

        rView.setHasFixedSize(true);
        rView.setLayoutManager(manager);
        rView.setAdapter(hAdapter);

        updateDisplay();
    }

    private void updateDisplay() {
        if(lDetails.size() == 0) {
            table_zone.setVisibility(View.GONE);
            notify_empty.setVisibility(View.VISIBLE);
        } else {
            table_zone.setVisibility(View.VISIBLE);
            notify_empty.setVisibility(View.GONE);
        }
    }
}