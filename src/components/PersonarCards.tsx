import PersonarCard from "./PersonarCard";
import axios from "axios";
import { PersonasData, FetchState } from "./../types";
import LocationPicker from "./LocationPicker";
import { useState } from "react";

const PersonarCards = () => {
  const [fetchRegion, setRegion] = useState("amber");
  const [fetchState, setFetchState] = useState(FetchState.DEFAULT);
  const [fetchPersonas, setPersonas] = useState<Array<PersonasData>>([]);

  const clickHandler = async () => {
    try {
      setFetchState(FetchState.LOADING);
      console.log(fetchRegion);
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
      <LocationPicker
        fetchRegion={fetchRegion}
        setRegion={setRegion}
      ></LocationPicker>

      {fetchState === FetchState.DEFAULT && (
        <>
          <p>Fetch personars</p>
          <button
            onClick={() => {
              clickHandler();
            }}
          >
            Get Posts
          </button>
        </>
      )}
      {fetchState === FetchState.LOADING && <p>Fetching posts...</p>}
      {fetchState === FetchState.ERROR && (
        <>
          <p>Oops! Something went wrong. Please try again.</p>
          <button
            onClick={() => {
              clickHandler();
            }}
          >
            Get Posts
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
            Get Posts
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
