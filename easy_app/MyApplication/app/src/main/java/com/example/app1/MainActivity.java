package com.example.app1;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText usn = findViewById(R.id.username);
        EditText psd = findViewById(R.id.password);
        EditText con_psd = findViewById(R.id.con_password);

        Button btn_reg = findViewById(R.id.btn_reg);
   4     btn_reg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String username = usn.getText().toString();
                String password = psd.getText().toString();
                String con_pasword = con_psd.getText().toString();
                if(username.isEmpty()){
                    Toast.makeText(MainActivity.this, "用户名不能为空", Toast.LENGTH_SHORT).show();
                } else if (password.isEmpty()) {
                    Toast.makeText(MainActivity.this, "密码不能为空", Toast.LENGTH_SHORT).show();
                } else if (!password.equals(con_pasword)) {
                    Toast.makeText(MainActivity.this, "两次输入密码不相同", Toast.LENGTH_SHORT).show();
                }else {
                    register_user(username,password);
                }
            }
        });
    }

    private void register_user(String username,String password) {
        OkHttpClient client = new OkHttpClient();

        String url = "https://a87302x371.vicp.fun/user/register";

        MediaType JSON = MediaType.get("application/json; charset=utf-8");
        JSONObject jsonBody = new JSONObject();
        try {
            jsonBody.put("username", username);
            jsonBody.put("password", password);
        } catch (JSONException e) {
            e.printStackTrace();
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    Toast.makeText(MainActivity.this, "Error building JSON", Toast.LENGTH_SHORT).show();
                }
            });
            return;
        }

        RequestBody body = RequestBody.create(JSON, jsonBody.toString());

        Request request = new Request.Builder()
                .url(url)
                .post(body)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (response.isSuccessful()) {
                    String responseBody = response.body().string();
                    try {
                        // 将响应体解析为JSON对象
                        JSONObject json = new JSONObject(responseBody);
                        String detail = json.getString("detail");
                        // 在TextView中显示message，或者您也可以使用Toast
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                Toast.makeText(MainActivity.this, detail, Toast.LENGTH_SHORT).show();
                            }
                        });

                    } catch (JSONException e) {
                        e.printStackTrace();
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                Toast.makeText(MainActivity.this,"json ERROR", Toast.LENGTH_SHORT).show();
                            }
                        });
                    }
                } else {
                    int statusCode = response.code();
                    String errorMessage = response.message();
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            Toast.makeText(MainActivity.this, "Error " + statusCode + ": " + errorMessage, Toast.LENGTH_SHORT).show();
                        }
                    });
                }
            }

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        Toast.makeText(MainActivity.this, "network ERROR", Toast.LENGTH_SHORT).show();
                    }
                });
            }
        });
    }
}