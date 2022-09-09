package com.example.topapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        var onCliquelogin = findViewById<Button>(R.id.login)
        onCliquelogin.setOnClickListener{
            //Recuperando o texto digitado pelo usuário e
            //atribuindo a uma String
            var txv_user = findViewById<EditText>(R.id.textUser)
            var txv_senha = findViewById<EditText>(R.id.textSenha)
            var txv_Resultado = findViewById<TextView>(R.id.falhaLogin)
            var nome:String = txv_user.editableText.toString()
            if (nome == "Matheus" || nome == "Vitoria") {
                val intent = Intent(this, LoginSucesso::class.java)
                intent.putExtra("usuario",nome)
                startActivity(intent)
            } else {
                txv_Resultado.text = "Falha Login"
            }
         //   val intent = Intent(this, Proxima::class.java)
        //    startActivity(intent)
        }
    }





    override fun onStart(){
        super.onStart()
        Log.i("onStart", "onStart Ativado")
    }

    override fun onResume(){
        super.onResume()
        Log.i("onResume", "onResume Ativado")
    }

    override fun onPause(){
        super.onPause()
        Log.i("onPause", "onPause Ativado")
    }

    override fun onStop(){
        super.onStop()
        Log.i("onStop", "onStop Ativado")
    }

    override fun onDestroy(){
        super.onDestroy()
        Log.i("onDestroy", "onDestroy Ativado")
    }}

