package com.example.football;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.SearchView;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import androidx.recyclerview.widget.StaggeredGridLayoutManager;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.text.InputType;
import android.text.method.PasswordTransformationMethod;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.navigation.NavigationView;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class MainActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener{

    private RecyclerView recyclerView;
    private FieldAdapter fAdapter;
    private SearchView search_bar;
    private ImageView list_display, grid_display;
    private TextView empty_notify;
    private List<FieldFB> fields = new ArrayList<>();
    private Toolbar toolbar;
    NavigationView navigationView;
    private DrawerLayout drawerLayout;
    private boolean flag_display = false;

    FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
    String userMail = user.getEmail();
    private RoomDB db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initVar();
        //nav
        navigationView.setNavigationItemSelectedListener(this);

        list_display.setOnClickListener(view -> {
            grid_display.setBackgroundColor(MainActivity.this.getResources().getColor(R.color.white));
            list_display.setBackgroundColor(MainActivity.this.getResources().getColor(R.color.select_layout_color));
            ListLayout(fields);
        });

        grid_display.setOnClickListener(view -> {
            flag_display = true;
            grid_display.setBackgroundColor(getResources().getColor(R.color.select_layout_color));
            list_display.setBackgroundColor(getResources().getColor(R.color.white));
            GridLayout(fields);
        });

        search_bar.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
            @Override
            public boolean onQueryTextSubmit(String s) {
                return false;
            }

            @Override
            public boolean onQueryTextChange(String s) {
                filterSearch(s);
                return false;
            }
        });
    }

    private void initVar() {
        recyclerView = findViewById(R.id.recyclerview);
        search_bar = findViewById(R.id.search_bar);
        list_display = findViewById(R.id.list_display);
        grid_display = findViewById(R.id.grid_display);
        empty_notify = findViewById(R.id.empty_notify);
        drawerLayout = findViewById(R.id.drawer_layout);
        navigationView = findViewById(R.id.nav_view);
        toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(this, drawerLayout, toolbar,
                R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();
        db = RoomDB.getInstance(this);

        if(db.fieldDAO().getSize() == 0) {
            for (int i = 1; i <= 8; i++) {
                FieldFB field = new FieldFB();
                field.setField_name("Sân số " + i);
                if(i <= 4) {
                    field.setField_type("Sân 5 người");
                }
                else {
                    field.setField_type("Sân 7 người");
                }
                db.fieldDAO().insert(field);
            }
        }
        fields.addAll(db.fieldDAO().getAll());
        ListLayout(fields);

        TextView tvDisplay = navigationView.getHeaderView(0).findViewById(R.id.display_user_name);
        tvDisplay.setText(userMail);
    }

    private void ListLayout(List<FieldFB> notes) {
        fAdapter = new FieldAdapter(MainActivity.this, fields, fieldClickListener);

        LinearLayoutManager manager = new LinearLayoutManager(MainActivity.this,
                LinearLayoutManager.VERTICAL,false);

        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(manager);
        recyclerView.setAdapter(fAdapter);
    }

    private void GridLayout(List<FieldFB> notes) {
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new StaggeredGridLayoutManager(2, LinearLayoutManager.VERTICAL));
        fAdapter = new FieldAdapter(MainActivity.this, notes, fieldClickListener);
        recyclerView.setAdapter(fAdapter);
    }

    private final FieldClickListener fieldClickListener = new FieldClickListener() {
        @Override
        public void onClick(FieldFB field) {
            Intent intent = new Intent(MainActivity.this, PickFieldActivity.class);
            intent.putExtra("id_field",field.getId());
            startActivity(intent);
        }
    };

    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        int id = item.getItemId();
        if(id == R.id.view_history) {
            startActivity(new Intent(MainActivity.this, HistoryPickActivity.class));
        }
        else if(id == R.id.change_password){
            startActivity(new Intent(MainActivity.this, ChangePasswordActivity.class));
        }else if(id == R.id.log_out){
            FirebaseAuth.getInstance().signOut();
            startActivity(new Intent(MainActivity.this, LoginActivity.class));
            finish();
        }

        drawerLayout.closeDrawer(GravityCompat.START);
        return true;
    }

    @Override
    public void onBackPressed() {
        if(drawerLayout.isDrawerOpen(GravityCompat.START)){
            drawerLayout.closeDrawer(GravityCompat.START);
        }else{
            super.onBackPressed();
        }
    }

    private void filterSearch(String s) {
        List<FieldFB> containList = new ArrayList<>();
        for(FieldFB field:fields) {
            if(field.getField_name().toLowerCase().contains(s.toLowerCase())
            || field.getField_type().toLowerCase().contains(s.toLowerCase())) {
                containList.add(field);
            }
        }
        fAdapter.filterList(containList);
        if(containList.size() == 0) {
            empty_notify.setVisibility(View.VISIBLE);
            empty_notify.setText("Không tìm thấy");
        }
        else {
            empty_notify.setVisibility(View.GONE);
        }
    }
}