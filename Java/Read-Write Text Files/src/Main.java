import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		System.out.println("PRIMEIRO METODO:");
		
		//LER O CONTEUDO DE UM FICHEIRO
		//PODE SER MELHOR POR VEZES ESPECIFICAR O PATH INTEIRO
		File f = new File("test.txt");
		Scanner scan = new Scanner(f);
		
		String fileContent = "";
		
		while(scan.hasNextLine()) {
			String currLine = scan.nextLine();
			fileContent = fileContent.concat(currLine + "\n");
			System.out.println(currLine);
		}
		
		//ESCREVER NUM FICHEIRO
		//PODE SER MELHOR POR VEZES ESPECIFICAR O PATH INTEIRO
		FileWriter fWriter = new FileWriter("testCopy.txt");
		fWriter.write(fileContent);
		
		System.out.println();//-------------------------------
		
		//LER UM ELEMENTO DE CADA VEZ DE UM FICHEIRO
		Scanner scanner = new Scanner(f);
		for(int i = 0; i < 3; i++) {
			String elem = scanner.next();
			System.out.println(i+1 + "º elemento: " + elem);
		}
		
		scan.close();
		scanner.close();
		fWriter.close();
		
		System.out.println("\nSEGUNDO METODO:");
		
		//UTILIZAR UM BUFFEREDWRITER PARA ESCREVER NUM FICHEIRO
		BufferedWriter bw = new BufferedWriter(new FileWriter("writing.txt"));
		bw.write("yaya\n");
		bw.write("yeye\n");
		bw.write("yiyi\n");
		bw.write("yoyo\n");
		bw.write("yuyu\n");
		bw.close();
		
		BufferedReader br = new BufferedReader(new FileReader("writing.txt"));
		
		String line;
		while( (line = br.readLine()) != null)
			System.out.println(line);
		
		br.close();
	}
	
}
