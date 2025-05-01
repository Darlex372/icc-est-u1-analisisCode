
import java.util.Random;

public class Benchmarking {
    private MetodosOrdenamiento ordenador ;
    public void Benchmarking() {
        long currentMills = System.currentTimeMillis();
        long currentNano = System.nanoTime();
        System.out.println("Current time in milliseconds: " + currentMills);
        System.out.println("Current time in nanoseconds: " + currentNano);
        ordenador = new MetodosOrdenamiento();
        int [] arreglo= generarArregloAleatorio(1000000);
        Runnable tarea =()-> ordenador.burbujaTradicional(arreglo);
        double tiempoduracionMillis= medirMills(tarea);
        double tiempoduracionNano= medirNanotime(tarea);
        System.out.println("Tiempo de duracion en Mills: " + tiempoduracionMillis);
        System.out.println("Tiempo de duracion en Nano: " + tiempoduracionNano);
    }
    private int [] generarArregloAleatorio(int n){
        /// desde el 0 al 99.999
        int [] arreglo = new int[n];
        Random random = new Random();

        for (int i = 0; i < n; i++){
            arreglo[i] = random.nextInt(100000);
           
        }
        return arreglo;
        
    }

    private double medirNanotime(Runnable tarea){
        
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        double segundos=  (fin-inicio)/1000000000.0;
        return segundos;

    }
    private double medirMills(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double segundos=  (fin-inicio)/1000.0;
        return segundos;
        
    }

    
    
}
