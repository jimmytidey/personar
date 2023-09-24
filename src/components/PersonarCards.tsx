import PersonarCard from "./PersonarCard";
import axios from "axios";
import { PersonasData, FetchState } from "./../types";
import { useState } from "react";

interface Props {
  fetchRegion: string;
}

const PersonarCards = ({ fetchRegion }: Props) => {
  const [fetchState, setFetchState] = useState(FetchState.DEFAULT);
  const [fetchPersonas, setPersonas] = useState<Array<PersonasData>>([]);

  const clickHandler = async () => {
    try {
      setFetchState(FetchState.LOADING);
      const res = await axios.get(
        import.meta.env.VITE_API_PATH + "/data/sample/?region=" + fetchRegion
      );
      const resData = res.data as Array<PersonasData>;
      setPersonas(resData);
      setFetchState(FetchState.SUCCESS);
    } catch (err) {
      setFetchState(FetchState.ERROR);
    }
  };

  return (
    <div>
      {fetchState === FetchState.DEFAULT && (
        <>
          <p>Fetch personars</p>
          <button
            onClick={() => {
              clickHandler();
            }}
          >
            Get Personas
          </button>
        </>
      )}
      {fetchState === FetchState.LOADING && <p>Fetching personas...</p>}
      {fetchState === FetchState.ERROR && (
        <>
          <p>Oops! Something went wrong. Please try again.</p>
          <button
            onClick={() => {
              clickHandler();
            }}
          >
            Get Personas
          </button>
        </>
      )}
      {fetchState === FetchState.SUCCESS && (
        <>
          <button
            onClick={() => {
              clickHandler();
            }}
          >
            Get Personas
          </button>
          <div className="container">
            {fetchPersonas.map((post, index) => (
              <PersonarCard key={index} postProps={post}></PersonarCard>
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default PersonarCards;
