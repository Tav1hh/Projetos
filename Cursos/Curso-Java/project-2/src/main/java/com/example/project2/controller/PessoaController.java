package com.example.project2.controller;

import com.example.project2.dto.CreatePessoaRequest;
import com.example.project2.dto.CreatePessoaResponse;
import com.example.project2.dto.Pessoa;
import com.example.project2.service.PessoaService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/pessoa")
public class PessoaController {

    private PessoaService pessoaService;

    @Autowired
    public void MyController(PessoaService pessoaService) {
        this.pessoaService = pessoaService;
    }

    @PostMapping("/save")
    private CreatePessoaResponse save(@Valid @RequestBody CreatePessoaRequest createPessoaRequest) {

        CreatePessoaResponse createPessoaResponse = new CreatePessoaResponse();
        Pessoa pessoa = new Pessoa();

        createPessoaResponse.setNome(createPessoaRequest.getNome());
        createPessoaResponse.setId(10L);


        pessoa.setCpf(createPessoaRequest.getCpf());
        pessoa.setNome(createPessoaRequest.getNome());
        pessoa.setIdade(createPessoaRequest.getIdade());
        pessoa.setId(createPessoaResponse.getId());

        pessoaService.save(pessoa);


        return  createPessoaResponse;
    }
}
