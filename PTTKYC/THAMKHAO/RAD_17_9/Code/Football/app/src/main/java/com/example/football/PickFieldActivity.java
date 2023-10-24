package com.example.football;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.app.DatePickerDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.text.InputType;
import android.text.method.PasswordTransformationMethod;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

public class PickFieldActivity extends AppCompatActivity implements View.OnClickListener {
    private ImageView backToPick;
    private TextView tv_name, tv_type, day_display;
    private TextView tv_time_f1, tv_time_f2, tv_time_f3, tv_time_f4;
    private TextView tv_price_f1,tv_price_f2, tv_price_f3, tv_price_f4;
    private TextView tv_state_f1, tv_state_f2, tv_state_f3, tv_state_f4;
    private Button btn_f1, btn_f2, btn_f3, btn_f4, btn_pickDay;
    int idField = 0;
    RoomDB db = RoomDB.getInstance(this);
    Button show;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pick_field);

        initVar();
        backToPick.setOnClickListener(this);
        btn_f1.setOnClickListener(this);
        btn_f2.setOnClickListener(this);
        btn_f3.setOnClickListener(this);
        btn_f4.setOnClickListener(this);
        show.setOnClickListener(this);

        btn_pickDay.setOnClickListener(view -> showDateSelectionDialog());
        Calendar calendar = Calendar.getInstance();
        int startYear = calendar.get(Calendar.YEAR);
        int startMonth = calendar.get(Calendar.MONTH);
        int startDay = calendar.get(Calendar.DAY_OF_MONTH);
        day_display.setText(startDay + "/" + (startMonth+1) + "/" + startYear);

        try {
            idField= (int) getIntent().getSerializableExtra("id_field");

        } catch (Exception e) {
            Log.e("NULL","can not get intent from main");
        }
        FieldFB field = db.fieldDAO().getFieldById(idField);
        tv_name.setText(field.getField_name());
        tv_type.setText(field.getField_type());

        if(field.getField_type().equals("Sân 5 người")) {
            tv_price_f1.setText(R.string.fr1_san5);
            tv_price_f2.setText(R.string.fr2_san5);
            tv_price_f3.setText(R.string.fr3_san5);
            tv_price_f4.setText(R.string.fr4_san5);
        } else {
            tv_price_f1.setText(R.string.fr1_san7);
            tv_price_f2.setText(R.string.fr2_san7);
            tv_price_f3.setText(R.string.fr3_san7);
            tv_price_f4.setText(R.string.fr4_san7);
        }
        updateTableDisplay();
    }

    private void showDateSelectionDialog() {
        Calendar c = Calendar.getInstance();

        int startYear = c.get(Calendar.YEAR);
        int startMonth = c.get(Calendar.MONTH);
        int startDay = c.get(Calendar.DAY_OF_MONTH);

        DatePickerDialog datePickerDialog = new DatePickerDialog(this, new DatePickerDialog.OnDateSetListener() {
            @Override
            public void onDateSet(DatePicker datePicker, int year, int monthOfYear, int dayOfMonth) {
                Calendar cal = Calendar.getInstance();
                cal.set(year,monthOfYear,dayOfMonth);
                if(c.getTimeInMillis() > cal.getTimeInMillis()) {
                    Toast.makeText(PickFieldActivity.this, "Không được chọn thời gian trong quá khứ", Toast.LENGTH_SHORT).show();
                }
                else {
                    day_display.setText(dayOfMonth + "/" + (monthOfYear+1) + "/" + year);
                    updateTableDisplay();
                }
            }
        }, startYear, startMonth, startDay);
        datePickerDialog.show();
        updateTableDisplay();
    }

    private void initVar() {
        backToPick = findViewById(R.id.backToPick);
        tv_name = findViewById(R.id.tv_name);
        tv_type = findViewById(R.id.tv_type);
        tv_time_f1 = findViewById(R.id.tv_time_f1);
        tv_time_f2 = findViewById(R.id.tv_time_f2);
        tv_time_f3 = findViewById(R.id.tv_time_f3);
        tv_time_f4 = findViewById(R.id.tv_time_f4);
        tv_price_f1 = findViewById(R.id.tv_price_f1);
        tv_price_f2 = findViewById(R.id.tv_price_f2);
        tv_price_f3 = findViewById(R.id.tv_price_f3);
        tv_price_f4 = findViewById(R.id.tv_price_f4);
        tv_state_f1 = findViewById(R.id.tv_state_f1);
        tv_state_f2 = findViewById(R.id.tv_state_f2);
        tv_state_f3 = findViewById(R.id.tv_state_f3);
        tv_state_f4 = findViewById(R.id.tv_state_f4);
        btn_pickDay = findViewById(R.id.btn_pickDay);
        day_display = findViewById(R.id.day_display);
        btn_f1 = findViewById(R.id.btn_f1);
        btn_f2 = findViewById(R.id.btn_f2);
        btn_f3 = findViewById(R.id.btn_f3);
        btn_f4 = findViewById(R.id.btn_f4);
        show = findViewById(R.id.show);
    }

    @Override
    protected void onResume() {
        super.onResume();
        updateTableDisplay();
    }

    private void updateTableDisplay() {
        List<PickDetail> listOfCurrentDay = db.detailDAO().getAllOrderByDateAndName(tv_name.getText().toString(),
                day_display.getText().toString());
        String ordered = "Đã được đặt";
        String available = "Còn sân";
        tv_state_f1.setText(available);
        tv_state_f2.setText(available);
        tv_state_f3.setText(available);
        tv_state_f4.setText(available);
        tv_state_f1.setTextColor(getResources().getColor(R.color.black));
        tv_state_f2.setTextColor(getResources().getColor(R.color.black));
        tv_state_f3.setTextColor(getResources().getColor(R.color.black));
        tv_state_f4.setTextColor(getResources().getColor(R.color.black));
        if(listOfCurrentDay.size() == 0) {
            tv_state_f1.setText(available);
            tv_state_f2.setText(available);
            tv_state_f3.setText(available);
            tv_state_f4.setText(available);
        }
        else {
            for(PickDetail pd:listOfCurrentDay) {
                if(pd.isTime_frame_1()) {
                    tv_state_f1.setText(ordered);
                    tv_state_f1.setTextColor(getResources().getColor(R.color.red));
                }

                if(pd.isTime_frame_2()) {
                    tv_state_f2.setText(ordered);
                    tv_state_f2.setTextColor(getResources().getColor(R.color.red));
                }

                if(pd.isTime_frame_3()) {
                    tv_state_f3.setText(ordered);
                    tv_state_f3.setTextColor(getResources().getColor(R.color.red));
                }

                if(pd.isTime_frame_4()) {
                    tv_state_f4.setText(ordered);
                    tv_state_f4.setTextColor(getResources().getColor(R.color.red));
                }
            }
        }
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.show:
                showDataInRoomDB();
                break;
            case R.id.backToPick:
                finish();
                break;
            case R.id.btn_f1:
                if(tv_state_f1.getText().toString().equals("Đã được đặt")) {
                    AlertDialog.Builder alert = new AlertDialog.Builder(PickFieldActivity.this);
                    final TextView tv = new TextView(PickFieldActivity.this);
                    alert.setTitle("Sân bạn chọn đã được đặt!");
                    alert.setMessage("Vui lòng thử chọn khung giờ khác hoặc sân khác");
                    alert.setView(tv);

                    alert.setPositiveButton("Xác nhận", new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int whichButton) {

                        }
                    });
                    alert.show();
                }
                else {
                    Intent intent = new Intent(this, ConfirmPickActivity.class);
                    intent.putExtra("id_field",idField);
                    intent.putExtra("frame_time",tv_time_f1.getText().toString());
                    intent.putExtra("price",tv_price_f1.getText().toString());
                    intent.putExtra("date_pick",day_display.getText().toString());
                    startActivity(intent);
                }
                break;
            case R.id.btn_f2:
                if(tv_state_f2.getText().toString().equals("Đã được đặt")) {
                    AlertDialog.Builder alert = new AlertDialog.Builder(PickFieldActivity.this);
                    final TextView tv = new TextView(PickFieldActivity.this);
                    alert.setTitle("Sân bạn chọn đã được đặt!");
                    alert.setMessage("Vui lòng thử chọn khung giờ khác hoặc sân khác");
                    alert.setView(tv);

                    alert.setPositiveButton("Xác nhận", new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int whichButton) {

                        }
                    });
                    alert.show();
                }
                else {
                    Intent intent = new Intent(this, ConfirmPickActivity.class);
                    intent.putExtra("id_field",idField);
                    intent.putExtra("frame_time",tv_time_f2.getText().toString());
                    intent.putExtra("price",tv_price_f2.getText().toString());
                    intent.putExtra("date_pick",day_display.getText().toString());
                    startActivity(intent);
                }
                break;
            case R.id.btn_f3:
                if(tv_state_f3.getText().toString().equals("Đã được đặt")) {
                    AlertDialog.Builder alert = new AlertDialog.Builder(PickFieldActivity.this);
                    final TextView tv = new TextView(PickFieldActivity.this);
                    alert.setTitle("Sân bạn chọn đã được đặt!");
                    alert.setMessage("Vui lòng thử chọn khung giờ khác hoặc sân khác");
                    alert.setView(tv);

                    alert.setPositiveButton("Xác nhận", new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int whichButton) {

                        }
                    });
                    alert.show();
                }
                else {
                    Intent intent = new Intent(this, ConfirmPickActivity.class);
                    intent.putExtra("id_field",idField);
                    intent.putExtra("frame_time",tv_time_f3.getText().toString());
                    intent.putExtra("price",tv_price_f3.getText().toString());
                    intent.putExtra("date_pick",day_display.getText().toString());
                    startActivity(intent);
                }
                break;
            case R.id.btn_f4:
                Log.e("OK","Btn4");
                if(tv_state_f4.getText().toString().equals("Đã được đặt")) {
                    AlertDialog.Builder alert = new AlertDialog.Builder(PickFieldActivity.this);
                    final TextView tv = new TextView(PickFieldActivity.this);
                    alert.setTitle("Sân bạn chọn đã được đặt!");
                    alert.setMessage("Vui lòng thử chọn khung giờ khác hoặc sân khác");
                    alert.setView(tv);

                    alert.setPositiveButton("Xác nhận", new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int whichButton) {

                        }
                    });
                    alert.show();
                }
                else {
                    Intent intent = new Intent(this, ConfirmPickActivity.class);
                    intent.putExtra("id_field",idField);
                    intent.putExtra("frame_time",tv_time_f4.getText().toString());
                    intent.putExtra("price",tv_price_f4.getText().toString());
                    intent.putExtra("date_pick",day_display.getText().toString());
                    startActivity(intent);
                }
                break;
        }
    }

    private void showDataInRoomDB() {
        for(PickDetail p:db.detailDAO().getAll()) {
            int i = p.getId();
            Log.e("TEST "+i, ""+p.getClient());
            Log.e("TEST "+i, ""+p.getUser_mail());
            Log.e("TEST "+i, ""+p.getField_name());
            Log.e("TEST "+i, ""+p.getField_type());
            Log.e("TEST "+i, ""+p.getDate_order());
            Log.e("TEST "+i, ""+p.getPrice());
            Log.e("TEST "+i, ""+p.isTime_frame_1());
            Log.e("TEST "+i, ""+p.isTime_frame_2());
            Log.e("TEST "+i, ""+p.isTime_frame_3());
            Log.e("TEST "+i, ""+p.isTime_frame_4());
            Log.e("newline","\n");
        }
    }
}