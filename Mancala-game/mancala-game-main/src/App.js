// import { useState, useEffect } from "react";
// import _ from "lodash";
// import { computeMove, checkWin } from "./lib/game";
// import PlayerSetup from "./components/PlayerSetup";
// import Field from "./components/Field";

// export const initialState = {
//   winner: false,
//   started: false,
//   turn: null,
//   players: [],
// };

// function App() {
//   const [state, setState] = useState(_.cloneDeep(initialState));

//   useEffect(() => {
//     if (
//       !state.winner &&
//       state.started &&
//       state.players[state.turn].type === "bot"
//     ) {
//       fetch("http://127.0.0.1:8000/result", {
//         method:"POST",
//         cache: "no-cache",
//         headers:{
//           "Content_Type":"application/json",
//           "Authorization": "Authorization"
//         },
//         body:JSON.stringify(state)
//       })
      

   
      
      
//       botMove();
      
//     }
//   });

//   function botMove() {
//     fetch("http://127.0.0.1:8000/content").then((res) =>
//     res.json().then((data) => {
//       console.log(data.index)
//       moveStones(data.index);   
//     })
//     );
//     // const { index } = state.players[state.turn].makeDecision(
//     //   _.cloneDeep(state)
//     // );
   
//   }

//   function moveStones(cellIndex) {
//     if (state.players[state.turn].field[cellIndex] === 0) {
//       console.log("You can not click on empty cell");
//       return;
//     }
//     if (cellIndex === 6) {
//       return;
//     }
//     setState((prevState) => {
//       const newState = computeMove(_.cloneDeep(prevState), cellIndex);
//       console.log(newState)
//       const [won, winner] = checkWin(newState);
//       return { ...prevState, ...newState, winner: won ? winner : false };
//     });
//   }

//   function startGame() {
//     if (state.players.length !== 2) {
//       console.log("You need to choose type of the players!");
//       return;
//     }
//     setState((p) => ({ ...p, started: true, turn: 0 }));
//   }

//   function restartGame() {
//     setState(_.cloneDeep(initialState));
//   }

//   return (
//     <div>
//       {!state.started || state.winner ? (
//         <div id="panel">
//           {!state.started && !state.winner ? (
//             <div className="select">
//               <PlayerSetup state={state} setState={setState} index={0} />
//               <PlayerSetup state={state} setState={setState} index={1} />
//             </div>
//           ) : (
//             ""
//           )}
//           {state.winner && (
//             <button onClick={() => restartGame()} className="m-auto btn">
//               New game
//             </button>
//           )}
//           {!state.started && state.players.length === 2 && (
//             <button onClick={() => startGame()} className="m-auto btn">
//               Start
//             </button>
//           )}
//         </div>
//       ) : (
//         ""
//       )}
//       {state.winner ? <h3>Game over, Player {state.winner.name} won!</h3> : ""}
//       {!state.started ? <h2>Choose players and press Start</h2> : ""}

//       <Field state={state} moveStones={moveStones} />
//       {state.started && !state.winner && (
//         <button
//           style={{ marginTop: "0.5rem" }}
//           onClick={() => restartGame()}
//           className="btn m-auto"
//         >
//           Reset game
//         </button>
//       )}
//     </div>
//   );
// }

// export default App;

import { useState, useEffect } from "react";
import _ from "lodash";
import { computeMove, checkWin } from "./lib/game";
import PlayerSetup from "./components/PlayerSetup";
import Field from "./components/Field";

export const initialState = {
  winner: false,
  begin:false,
  started: false,
  turn: null,
  players: [],
};

function App() {
  
  
  const [state, setState] = useState(_.cloneDeep(initialState));
  const [isActive, setIsActive] = useState(false);


  const getName =  async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/content')
        if (!response.ok) {
          throw new Error('Data coud not be fetched!')
        }
        const resp = await response.json();
        console.log("Obj returned from server", resp)
        if(resp.move> 0 & resp.move<6  ){

          moveStones(resp.move)          

        }
        
    } 
    catch (error) {
     console.log(error)
    }
   }
  useEffect(() => {
    if (
      !state.winner &&
      state.started &&
      state.players[state.turn].type === "bot"
    ) {
      fetch("http://127.0.0.1:8000/result", {
        method:"POST",
        cache: "no-cache",
        headers:{
          "Content_Type":"application/json",
          "Authorization": "Authorization"
        },
        body:JSON.stringify(state)
      })
      
      
       
      getName()
  }
  });

  function moveStones(cellIndex) {
    if (state.players[state.turn].field[cellIndex] === 0) {
      return ;
    }
    if (cellIndex === 6) {
      return;
    }
    setState((prevState) => {
      const newState = _.cloneDeep(computeMove(_.cloneDeep(prevState), cellIndex));
      const [won, winner] = checkWin(newState);
      console.log("type",state.players[state.turn].type ,"turn !", state.players[state.turn].index);
      return { ...prevState, ...newState, winner: won ? winner : false };
    });
  }

  function startGame() {
    setIsActive(current => !current);
    if (state.players.length !== 2) {
      return;
    }
    setState((p) => ({ ...p, started: true, turn:0}));
    
  }

  function restartGame() {
    setState(_.cloneDeep(initialState));
  }

  return (
   
    <div  style={
      { 
      
      backgroundColor: isActive ? '#080A40' : '',
      backgroundPosition: 'center',
      backgroundSize: 'cover',
      backgroundRepeat: 'no-repeat',
      width: '100vw',
      height: '100vh'  
      
    }}>
      
      
      {!state.started || state.winner ?  (
        <div id="panel"
       style ={{ marginTop: '10rem',                   opacity: isActive ? '1' : '',
      }}
        

        >
          {!state.started && !state.winner ? (
            <div className="select"
            style={{color:"#FFFFFF",

          }}
           
            >
              <PlayerSetup   state={state} setState={setState} index={0} />
              <PlayerSetup state={state} setState={setState} index={1} />
            </div>
          ) : (
            ""
          )}
          {state.winner && (
            <button onClick={() => restartGame()} className="m-auto btn">
              New game
            </button>
          )}
          {!state.started && state.players.length === 2 && (
            <button onClick={() => startGame()} className="m-auto btn">
              Start
            </button>
          )}
      
        </div>
      ) : (
        ""
      )}
      <div   style={
        { 
          height: '100vh', 
          display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'column',
      marginLeft: "17rem"   
    }}>
      {state.winner ? <h3>Game over, Player {state.winner.name} won!</h3> : ""}
      
 
       <Field   state={state} moveStones={moveStones} />
      {state.started && !state.winner && (
        <button
          style={{ marginTop: "0.9rem",marginLeft:"20rem" }}
          onClick={() => restartGame()}
          className="btn m-auto"
        >
          Reset game
        </button>
      )}

      </div>

     
    </div>
   
  );
}

export default App;