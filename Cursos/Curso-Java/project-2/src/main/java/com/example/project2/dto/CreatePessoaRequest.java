package com.example.project2.dto;

import jakarta.validation.constraints.NotEmpty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CreatePessoaRequest {

    @NotEmpty(message = "Nome não pode ficar vazio!")
    private String nome;
    private Integer idade;
    private String cpf;
}
