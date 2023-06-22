import java.util.Random;

public class AlgoritmoGenetico {

    // Define o tamanho da população e o número de gerações
    private static final int TAMANHO_POPULACAO = 10;
    private static final int NUM_GERACOES = 100;
    
    // Define a taxa de mutação (em porcentagem)
    private static final double TAXA_MUTACAO = 0.1;
    
    // Define o número de genes em cada indivíduo
    private static final int NUM_GENES = 5;
    
    // Define o valor máximo e mínimo de cada gene
    private static final int VALOR_MINIMO = 0;
    private static final int VALOR_MAXIMO = 31;
    
    // Define o número de bits necessários para representar cada gene
    private static final int NUM_BITS = 5;

    // Define a função de fitness que calcula a aptidão de um indivíduo
    private static double fitness(int[] individuo) {
        double aptidao = 0;
        for (int i = 0; i < NUM_GENES; i++) {
            aptidao += individuo[i];
        }
        return aptidao;
    }

    // Seleciona dois indivíduos aleatórios para cruzamento
    private static int[][] selecaoTorneio(int[][] populacao) {
        int[][] pais = new int[2][NUM_GENES];
        for (int i = 0; i < 2; i++) {
            int indice1 = new Random().nextInt(TAMANHO_POPULACAO);
            int indice2 = new Random().nextInt(TAMANHO_POPULACAO);
            pais[i] = populacao[indice1][1] > populacao[indice2][1] ? populacao[indice1] : populacao[indice2];
        }
        return pais;
    }

    // Executa o cruzamento de dois indivíduos para gerar um novo
    private static int[] cruzamento(int[] pai1, int[] pai2) {
        int[] filho = new int[NUM_GENES];
        int pontoDeCorte = new Random().nextInt(NUM_GENES);
        for (int i = 0; i < pontoDeCorte; i++) {
            filho[i] = pai1[i];
        }
        for (int i = pontoDeCorte; i < NUM_GENES; i++) {
            filho[i] = pai2[i];
        }
        return filho;
    }

    // Executa a mutação em um indivíduo
    private static void mutacao(int[] individuo) {
        for (int i = 0; i < NUM_GENES; i++) {
            if (new Random().nextDouble() < TAXA_MUTACAO) {
                individuo[i] = new Random().nextInt(VALOR_MAXIMO - VALOR_MINIMO + 1) + VALOR_MINIMO;
            }
        }
    }

    // Executa o algoritmo genético
    public static void main(String[] args) {
        // Inicializa a população de forma aleatória
        int[][] populacao = new int[TAMANHO_POPULACAO][NUM_GENES];
        for (int i = 0; i < TAMANHO_POPULACAO; i++) {
            for (int j = 0; j < NUM_GENES; j++){
                 // Gera um número aleatório de acordo com o número de bits
                 String gene = Integer.toBinaryString(new Random().nextInt(VALOR_MAXIMO - VALOR_MINIMO + 1) + VALOR_MINIMO);
                // Completa o número com zeros à esquerda, se necessário
                while (gene.length() < NUM_BITS) {
                gene = "0" + gene;
                }
                // Converte o gene de volta para um número inteiro e o adiciona ao indivíduo
                populacao[i][j] = Integer.parseInt(gene, 2);
                }
            }
                        
            // Executa o algoritmo genético por um número fixo de gerações
            for (int geracao = 0; geracao < NUM_GERACOES; geracao++) {
                // Calcula a aptidão de cada indivíduo na população
                double[] aptidoes = new double[TAMANHO_POPULACAO];
                for (int i = 0; i < TAMANHO_POPULACAO; i++) {
                    aptidoes[i] = fitness(populacao[i]);
                    }
                            
                // Seleciona dois pais para cruzamento através do método do torneio
                int[][] pais = selecaoTorneio(populacao);
                            
                // Executa o cruzamento para gerar um novo filho
                int[] filho = cruzamento(pais[0], pais[1]);
                            
                // Executa a mutação no filho, se necessário
                mutacao(filho);
                            
                // Encontra o indivíduo menos apto na população e o substitui pelo filho gerado
                int indiceMenosApto = 0;
                for (int i = 1; i < TAMANHO_POPULACAO; i++) {
                    if (aptidoes[i] < aptidoes[indiceMenosApto]) {
                        indiceMenosApto = i;
                        }
                    }
                populacao[indiceMenosApto] = filho;
                            
                // Imprime a aptidão do melhor indivíduo na geração atual
                double melhorAptidao = 0;
                 for (int i = 0; i < TAMANHO_POPULACAO; i++) {
                    if (aptidoes[i] > melhorAptidao) {
                        melhorAptidao = aptidoes[i];
                        }
                    }
                System.out.println("Geração " + geracao + ": Melhor aptidão = " + melhorAptidao);
            }
    }
}
