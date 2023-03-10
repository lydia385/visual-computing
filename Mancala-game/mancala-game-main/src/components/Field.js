import React from "react";

export default function Field({ state, moveStones  }) {
  return state.players.map((player, j) => (
    <div key={Date.now() + Math.random().toFixed(j)} className="row">
      {!player.reversed && <div className="hidden-cell cell" />}
      { 
       player.getField().map((stones, i) => (
        <div
          key={Date.now() + Math.random().toFixed(i)}
          className={`${state.turn !== j ? "disabled" : ""} cell`}
          onClick={() =>
            state.turn ===1 && moveStones(player.reversed ? 6 - i : i) && state.players[1].index === 1
          }
        >
          {stones}
          
        </div>
      ))}
    </div>
  ));
}
