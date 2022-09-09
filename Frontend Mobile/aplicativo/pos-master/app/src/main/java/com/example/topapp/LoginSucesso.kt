package com.example.topapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ImageButton
import android.widget.TextView
class LoginSucesso  : AppCompatActivity()  {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.loginsucesso)



        var txv_Resultado = findViewById<TextView>(R.id.textView3)

        val valor:String = intent.getStringExtra("usuario").toString()
        txv_Resultado.text = valor



        var onCliquedentista = findViewById<ImageButton>(R.id.botaodentista)
        onCliquedentista.setOnClickListener{
            val intent = Intent(this, Dentista::class.java)
            startActivity(intent)
    }
        var onCliquemedico = findViewById<ImageButton>(R.id.botaomedico)
        onCliquemedico.setOnClickListener{
            val intent = Intent(this, Medico::class.java)
            startActivity(intent)
        }


    }}
