package com.example.football;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.AppCompatButton;

import android.content.Intent;
import android.os.Bundle;
import android.util.Patterns;
import android.view.View;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class LoginActivity extends AppCompatActivity implements View.OnClickListener {

    private FirebaseAuth mAuth;
    private EditText user_email;
    private EditText user_password;
    private AppCompatButton btn_sign_in;
    private TextView sign_up;
    private TextView forgot_pass;
    private ProgressBar progressBar_login;
    FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        initVar();
        btn_sign_in.setOnClickListener(this);
        sign_up.setOnClickListener(this);
        forgot_pass.setOnClickListener(this);
        if(user!= null) {
            startActivity(new Intent(LoginActivity.this, MainActivity.class));
            progressBar_login.setVisibility(View.INVISIBLE);
            finish();
        }
        else {
            progressBar_login.setVisibility(View.INVISIBLE);
        }

    }

    @Override
    public void onClick(View view) {
        switch(view.getId()) {
            case R.id.btn_sign_in:
                loginAction();
                break;
            case R.id.sign_up:
                startActivity(new Intent(LoginActivity.this, RegisterActivity.class));
                break;
            case R.id.forgot_pass:
                startActivity(new Intent(LoginActivity.this, ForgotActivity.class));
                break;
        }
    }

    private void loginAction() {
        String email = user_email.getText().toString();
        String pass = user_password.getText().toString();

        if(email.equals("")) {
            user_email.setError("Vui lòng nhập email");
            user_email.requestFocus();
            return;
        }
        else if(!Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
            user_email.setError("Vui lòng cung cấp email hợp lệ");
            user_email.requestFocus();
            return;
        }
        else if(pass.equals("")) {
            user_password.setError("Vui lòng nhập mật khẩu");
            user_password.requestFocus();
            return;
        }
        else if(pass.contains(" ")) {
            user_password.setError("Mật khẩu không được chứa khoảng trắng");
            user_password.requestFocus();
            return;
        }
        else if(pass.length() < 8) {
            user_password.setError("Mật khẩu phải có ít nhất 8 kí tự");
            user_password.requestFocus();
            return;
        }
        else {
            progressBar_login.setVisibility(View.VISIBLE);
            mAuth.signInWithEmailAndPassword(email,pass).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                @Override
                public void onComplete(@NonNull Task<AuthResult> task) {
                    if(task.isSuccessful()) {
                        progressBar_login.setVisibility(View.INVISIBLE);
                        Intent intent = new Intent(LoginActivity.this, MainActivity.class);
                        startActivity(intent);
                        finish();
                    }
                    else {
                        Toast.makeText(LoginActivity.this, "Email hoặc mật khẩu không đúng", Toast.LENGTH_SHORT).show();
                        progressBar_login.setVisibility(View.INVISIBLE);
                    }
                }
            });
        }
    }

    private void initVar() {
        mAuth = FirebaseAuth.getInstance();
        user_email = findViewById(R.id.user_email);
        user_password = findViewById(R.id.user_password);
        btn_sign_in = findViewById(R.id.btn_sign_in);
        sign_up = findViewById(R.id.sign_up);
        forgot_pass = findViewById(R.id.forgot_pass);
        progressBar_login = findViewById(R.id.progressBar_login);
    }
}