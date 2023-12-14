class Solution {
    public int[] timeTaken(int[] arrival, int[] state) {
        int n = arrival.length; 
        int currentTime = 0;
        int lastEnterTime = -10;
        Integer nextToEnter = findNextToEnter(0, state);
        Integer nextToExit = findNextToExit(0, state);
        int[] answer = new int[n];

        while (nextToEnter != null && nextToExit != null) {
            if (arrival[nextToEnter] > currentTime && arrival[nextToExit] > currentTime) {
                currentTime = Math.min(arrival[nextToEnter], arrival[nextToExit]);
            }

            if (arrival[nextToEnter] <= currentTime 
                    && (arrival[nextToExit] > currentTime || lastEnterTime == currentTime - 1)) {
                answer[nextToEnter] = currentTime;
                nextToEnter = findNextToEnter(nextToEnter + 1, state);
                lastEnterTime = currentTime;
                currentTime++;
            } else {
                answer[nextToExit] = currentTime;
                nextToExit = findNextToExit(nextToExit + 1, state);
                currentTime++;
            }
        }

        while (nextToEnter != null) {
            if (arrival[nextToEnter] > currentTime) {
                currentTime = arrival[nextToEnter];
            }
            answer[nextToEnter] = currentTime;
            nextToEnter = findNextToEnter(nextToEnter + 1, state);
            currentTime++;
        }

        while (nextToExit != null) {
            if (arrival[nextToExit] > currentTime) {
                currentTime = arrival[nextToExit];
            }
            answer[nextToExit] = currentTime;
            nextToExit = findNextToExit(nextToExit + 1, state);
            currentTime++;
        }

        return answer;
    }

    private Integer findNextToEnter(int start, int[] state) {
        int i = start;
        while (i < state.length && state[i] != 0) {
            i++;
        }
        return i == state.length ? null : i;
    }

    private Integer findNextToExit(int start, int[] state) {
        int i = start;
        while (i < state.length && state[i] != 1) {
            i++;
        }
        return i == state.length ? null : i;
    }
}