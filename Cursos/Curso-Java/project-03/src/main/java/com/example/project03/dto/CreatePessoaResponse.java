package com.example.project03.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CreatePessoaResponse {
    String nome;
    String senha;
    Integer idade;
    String cpf;
    String endereco;
}
