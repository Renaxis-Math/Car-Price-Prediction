import java.util.List;
import java.util.Queue;
import java.util.LinkedList;

class Result {

    /*
     * Complete the 'getResult' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY arrival
     *  2. INTEGER_ARRAY direction
     */

    public static List<Integer> getResult(List<Integer> arrival, List<Integer> direction) {
        // two pointers to track the next person that wants to enter and the next person that wants to exit.
        Queue<Integer> queue_enter = new LinkedList<>();
        Queue<Integer> queue_exit = new LinkedList<>();

        int n = arrival.size(), last = -1, t = 0, tot = n, i = 0;
        int[] res = new int[n];
        while (tot > 0) { // record the current status of door possession
            if (queue_enter.isEmpty() && queue_exit.isEmpty() && i < n) {
                if (t != arrival.get(i)) {
                    last = -1;
                    t = arrival.get(i);
                }
            }
            while (i < n && arrival.get(i) <= t) {
                if (direction.get(i) == 0) queue_enter.offer(i);
                else queue_exit.offer(i);
                i++;
            }

            if (last == -1) { // No one is using
                if (!queue_exit.isEmpty()) {
                    res[queue_exit.poll()] = t;
                    last = 1;
                }
                else {
                    res[queue_enter.poll()] = t;
                    last = 0;
                }
            } else if (last == 0) { // Someone is entering
                if (!queue_enter.isEmpty()) {
                    res[queue_enter.poll()] = t;
                    last = 0;
                } else {
                    res[queue_exit.poll()] = t;
                    last = 1;
                }
            } else { // Someone is exiting
                if (!queue_exit.isEmpty()) {
                    res[queue_exit.poll()] = t;
                    last = 1;
                } else {
                    res[queue_enter.poll()] = t;
                    last = 0;
                }
            }
            t++;
            tot--;
        }
        return Arrays.stream(res).boxed().collect(Collectors.toList());
    }
}