import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Program {

  public static void main(String[] args) throws Exception {
    for (int noun = 0; noun <= 99; noun += 1) {
      for (int verb = 0; verb <= 99; verb += 1) {
        Path path = Path.of("input.txt");
        List<Integer> code = Arrays
          .stream(Files.readAllLines(path).get(0).split(","))
          .map((input) -> Integer.parseInt(input))
          .collect(Collectors.toList());
    
        code.set(1, noun);
        code.set(2, verb);
    
        Integer current = 0;
        while (true) {
          Integer operation = code.get(current);
          if (operation == 99)
            break;
    
          Integer locationA = code.get(current + 1);
          Integer locationB = code.get(current + 2);
          Integer locationC = code.get(current + 3);
          Integer valueA = code.get(locationA);
          Integer valueB = code.get(locationB);
          Integer result = 0;
          switch (operation) {
            case 1:
              result = valueA + valueB;
              break;
            case 2:
              result = valueA * valueB;
              break;
          }
          code.set(locationC, result);
          current += 4;
        }
        
        if (code.get(0) == 19690720) {
          System.out.println("Success at noun:" + noun + " and verb:" + verb);
        }
      }
    }
  }
}
