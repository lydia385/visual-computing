import { minimaxWithPrunning } from "../lib/ai";

export default class Player {
  constructor(index, name, reversed = false, playerType) {
    this.name = name;
    this.field = [4, 4, 4, 4, 4, 4, 0];
    this.reversed = reversed;
    this.type = playerType;
    this.lvl = 1;
    this.index = index;
  }

  getField() {
    return this.reversed ? [...this.field].reverse() : this.field;
  }

  makeDecision(state) {
    // flask here : instead of return we flask it with python
    return minimaxWithPrunning(-Infinity, Infinity, 0, true, state, this.lvl, this.index);
  }
}
