import java.util.concurrent.TimeUnit;

class Main
{
    public static void move(int disks, int source, int auxiliary, int target)
    {
        if (disks > 0)
        {
            // déplace les disques `n-1` de la source vers l'auxiliaire en utilisant la cible
            // comme pôle intermédiaire
            move(disks - 1, source, target, auxiliary);
 
            // déplacer un disque de la source à la cible
            System.out.println("Disque " + disks + " de " + source + " a " +
                                target);
 
            // déplace les disques `n-1` de l'auxiliaire vers la cible en utilisant la source
            // comme pôle intermédiaire
            move(disks - 1, auxiliary, source, target);

          
        }
    }
 
    // Problème de la tour de Hanoï
    public static void main(String[] args)
    {
        int n = 23;
      
        long startTime = System.nanoTime();
        move(n, 1, 2, 3);
 
        long endTime = System.nanoTime();

        long timeElapsed = endTime - startTime;

        System.out.println("Total elapsed time in execution of method callMethod() seconde is :"+ ((timeElapsed)/1000000000));

    }
}
