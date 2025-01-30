package cursojava;
import java.util.Scanner;

public class App{
    @SuppressWarnings("resource")
    public static void main(String[] args){
        //Declara o fluxo (stream) de entrada de dados.
        Scanner in = new Scanner(System.in);

        //Declaração das variaveis.
        String nome;
        int idade;

        //Mostra um cabeçalho de saida.
        System.out.println("**** Programa Cadastro V. 0.01 ****");

        //Pega os dados do úsuario.
        System.out.print("Digite seu nome completo: ");
        nome = in.nextLine();
        System.out.print("Digite sua idade: ");
        idade = in.nextInt();

        //Mostra na tela o nome e a idade.
        System.out.println("Usuario: " +nome+"\nIdade: "+idade);

    }
}