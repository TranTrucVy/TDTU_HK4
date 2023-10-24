package com.example.football;

import androidx.activity.ComponentActivity;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.FirebaseException;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseAuthInvalidCredentialsException;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.auth.PhoneAuthCredential;
import com.google.firebase.auth.PhoneAuthOptions;
import com.google.firebase.auth.PhoneAuthProvider;

import java.lang.reflect.Field;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class ConfirmPickActivity extends AppCompatActivity {

    TextView field_name_pick, tv_frame_pick, tv_time_pick, tv_price_pick, tv_type_pick, resendOTP;
    EditText name_client, phone_number_client, edt_otp_code;
    LinearLayout backToPick, zone_confirm;
    Button btn_confirm_info, btn_confirm_OTP;
    RoomDB db = RoomDB.getInstance(this);
    FirebaseAuth mAuth;
    FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
//    String phone_number, mVerificationId;
//    private PhoneAuthProvider.ForceResendingToken mResendToken;
    ProgressDialog dialog;
    private static final String TAG = ConfirmPickActivity.class.getName();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_confirm_pick);

        initVar();

        int id = (int) getIntent().getSerializableExtra("id_field");
        String frame = (String) getIntent().getSerializableExtra("frame_time");
        String price = (String) getIntent().getSerializableExtra("price");
        String date_order = (String) getIntent().getSerializableExtra("date_pick");
        FieldFB ffb = db.fieldDAO().getFieldById(id);
        field_name_pick.setText(ffb.getField_name());
        tv_type_pick.setText(ffb.getField_type());
        tv_frame_pick.setText(frame);
        tv_time_pick.setText(date_order);
        tv_price_pick.setText(price);

        backToPick.setOnClickListener(view -> finish());

        btn_confirm_info.setOnClickListener(view -> {
            if(name_client.getText().toString().equals("")
                    || name_client.getText().toString().equals(" ")) {
                name_client.setError("Vui lòng nhập họ và tên");
                name_client.requestFocus();
            }
            else if(phone_number_client.getText().toString().equals("")
                    || phone_number_client.getText().toString().equals(" ")) {
                phone_number_client.setError("Vui lòng nhập số điện thoại");
                phone_number_client.requestFocus();
            }
            else {
                try {
                    PickDetail pickDetail = new PickDetail();
                    pickDetail.setClient(name_client.getText().toString());
                    pickDetail.setUser_mail(user.getEmail());
                    pickDetail.setField_name(ffb.getField_name());
                    pickDetail.setField_type(ffb.getField_type());
                    pickDetail.setDate_order(date_order);
                    pickDetail.setPrice(price);
                    pickDetail.setPhone_num_client(phone_number_client.getText().toString());
                    switch (frame) {
                        case "7h - 8h30":
                            pickDetail.setTime_frame_1(true);
                            break;
                        case "16h - 17h30":
                            pickDetail.setTime_frame_2(true);
                            break;
                        case "18h - 19h30":
                            pickDetail.setTime_frame_3(true);
                            break;
                        case "19h45 - 21h15":
                            pickDetail.setTime_frame_4(true);
                            break;
                    }
                    if(db.detailDAO().getAllForCheckInsert(ffb.getField_name(),
                            date_order,price).size() == 0) {
                        db.detailDAO().insert(pickDetail);
                    }
                    showDataInRoomDB();
                    Toast.makeText(this, "Đặt sân thành công", Toast.LENGTH_SHORT).show();
                    finish();
//                    zone_confirm.setVisibility(View.VISIBLE);
//                    String phoneNumber = "+84"+phone_number_client.getText().toString();
                    /*FirebaseAuth.getInstance().getFirebaseAuthSettings()
                            .setAppVerificationDisabledForTesting(true);*/
//                    onClickVerifyPhoneNumber(phoneNumber);
                } catch (Exception e) {
                    Toast.makeText(this, "Có lỗi xảy ra, không thành công", Toast.LENGTH_SHORT).show();
                }
            }
        });

        /*btn_confirm_OTP.setOnClickListener(view -> {
            String otp_code = edt_otp_code.getText().toString().trim();
//            onClickSendOtpCode(otp_code);
        });*/

        /*resendOTP.setOnClickListener(view -> {
            onClickSendOtpAgain();
        });*/
    }

    /*private void onClickSendOtpAgain() {
        PhoneAuthOptions options =
                PhoneAuthOptions.newBuilder(mAuth)
                        .setPhoneNumber(phone_number)
                        .setTimeout(60L, TimeUnit.SECONDS)
                        .setActivity(this)
                        .setForceResendingToken(mResendToken)
                        .setCallbacks(new PhoneAuthProvider.OnVerificationStateChangedCallbacks() {
                            @Override
                            public void onVerificationCompleted(@NonNull PhoneAuthCredential phoneAuthCredential) {
                                Toast.makeText(ConfirmPickActivity.this, "onVerificationSuccess", Toast.LENGTH_SHORT).show();
                                signInWithPhoneAuthCredential(phoneAuthCredential);
//                                dialog.dismiss();
                            }

                            @Override
                            public void onVerificationFailed(@NonNull FirebaseException e) {
                                Toast.makeText(ConfirmPickActivity.this, "onVerificationFailed", Toast.LENGTH_SHORT).show();
//                                dialog.dismiss();
                            }

                            @Override
                            public void onCodeSent(@NonNull String verificationId, @NonNull PhoneAuthProvider.ForceResendingToken forceResendingToken) {
                                super.onCodeSent(verificationId, forceResendingToken);
                                mVerificationId = verificationId;
                                mResendToken = forceResendingToken;
                            }
                        })
                        .build();
        PhoneAuthProvider.verifyPhoneNumber(options);
    }*/

    /*private void onClickSendOtpCode(String otp_code) {
        PhoneAuthCredential credential = PhoneAuthProvider.getCredential(mVerificationId, otp_code);
        signInWithPhoneAuthCredential(credential);
    }

    private void onClickVerifyPhoneNumber(String phoneNumber) {
        phone_number = phoneNumber;
        PhoneAuthOptions options =
                PhoneAuthOptions.newBuilder(mAuth)
                        .setPhoneNumber(phoneNumber)
                        .setTimeout(60L, TimeUnit.SECONDS)
                        .setActivity(this)
                        .setCallbacks(new PhoneAuthProvider.OnVerificationStateChangedCallbacks() {
                            @Override
                            public void onVerificationCompleted(@NonNull PhoneAuthCredential phoneAuthCredential) {
                                signInWithPhoneAuthCredential(phoneAuthCredential);
                            }

                            @Override
                            public void onVerificationFailed(@NonNull FirebaseException e) {
                                Toast.makeText(ConfirmPickActivity.this, e.getMessage(), Toast.LENGTH_SHORT).show();
                            }

                            @Override
                            public void onCodeSent(@NonNull String verificationId, @NonNull PhoneAuthProvider.ForceResendingToken token) {
//                                super.onCodeSent(verificationId, token);
                                Log.e(TAG,"onCodeSent:" + verificationId);
                                mVerificationId = verificationId;
                                mResendToken = token;
                            }
                        })
                        .build();
        PhoneAuthProvider.verifyPhoneNumber(options);
    }

    private void signInWithPhoneAuthCredential(PhoneAuthCredential credential) {
        mAuth.signInWithCredential(credential)
                .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if (task.isSuccessful()) {
                            Log.e("TAG", "signInWithCredential:success");
                            FirebaseUser user = task.getResult().getUser();
                            startActivity(new Intent(ConfirmPickActivity.this, PickFieldActivity.class));
                        } else {
                            Toast.makeText(ConfirmPickActivity.this, task.getException().getMessage(), Toast.LENGTH_SHORT).show();
                            if (task.getException() instanceof FirebaseAuthInvalidCredentialsException) {
                                Toast.makeText(ConfirmPickActivity.this, "Invalid", Toast.LENGTH_SHORT).show();
                            }
                        }
                    }
                });
    }*/

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

    private void initVar() {
        name_client = findViewById(R.id.name_client);
        phone_number_client = findViewById(R.id.phone_number_client);
        btn_confirm_info = findViewById(R.id.btn_confirm_info);
        field_name_pick = findViewById(R.id.field_name_pick);
        tv_frame_pick = findViewById(R.id.tv_frame_pick);
        tv_time_pick = findViewById(R.id.tv_time_pick);
        tv_price_pick = findViewById(R.id.tv_price_pick);
        tv_type_pick = findViewById(R.id.tv_type_pick);
        backToPick = findViewById(R.id.backToPick);
        zone_confirm = findViewById(R.id.zone_confirm);
        edt_otp_code = findViewById(R.id.edt_otp_code);
        btn_confirm_OTP = findViewById(R.id.btn_confirm_OTP);
        resendOTP = findViewById(R.id.resendOTP);
        mAuth = FirebaseAuth.getInstance();
        dialog = new ProgressDialog(this);
    }
}