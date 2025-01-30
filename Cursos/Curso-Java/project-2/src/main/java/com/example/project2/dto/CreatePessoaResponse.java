package com.example.project2.dto;

import jakarta.validation.constraints.NotEmpty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CreatePessoaResponse {

    private String nome;
    private Long id;

}
