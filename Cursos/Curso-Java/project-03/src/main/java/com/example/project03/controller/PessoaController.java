package com.example.project03.controller;

import com.example.project03.dto.CreatePessoaRequest;
import com.example.project03.dto.CreatePessoaResponse;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PessoaController {

    @PostMapping("/getUser")
    public CreatePessoaResponse getUser(@RequestBody CreatePessoaRequest createPessoaRequest) {
        //Estancia o Objeto Response que vai retornar ao Front
        CreatePessoaResponse createPessoaResponse = new CreatePessoaResponse();

        //Pega as informações para retornar ao úsuario
        createPessoaResponse.setNome(createPessoaRequest.getNome());
        createPessoaResponse.setSenha(createPessoaRequest.getSenha());
        createPessoaResponse.setIdade(18);
        createPessoaResponse.setCpf("123.456.789.10");
        createPessoaResponse.setEndereco("Rua das jabuticabeiras");

        //Retorna os Objeto Response com os dados ao Front
        return createPessoaResponse;
    }
}
