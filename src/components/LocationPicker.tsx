import { FetchState, LtlaListData } from "../types";
import axios from "axios";
import { useEffect, useState } from "react";

interface Props {
  fetchRegion: string;
  setRegion: Function;
}

const LocationPicker = ({ fetchRegion, setRegion }: Props) => {
  const [fetchState, setFetchState] = useState(FetchState.DEFAULT);
  const [LtlaList, setLtlaList] = useState<Array<LtlaListData>>([]);
  const getLtlaList = async () => {
    try {
      setFetchState(FetchState.LOADING);

      const res = await axios.get(
        import.meta.env.VITE_API_PATH + "/data/list_ltlas/"
      );
      const resData = res.data as Array<LtlaListData>;

      setLtlaList(resData);
      setFetchState(FetchState.SUCCESS);
    } catch (err) {
      setFetchState(FetchState.ERROR);
    }
  };

  useEffect(() => {
    getLtlaList();
  }, []);

  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setRegion(event.target.value);
  };

  return (
    <div>
      {fetchState === FetchState.DEFAULT && (
        <>
          <p>Loading location picker...</p>
        </>
      )}
      {fetchState === FetchState.LOADING && <p>Fetching posts...</p>}
      {fetchState === FetchState.ERROR && (
        <>
          <p>Error loading location picker .</p>
        </>
      )}
      {fetchState === FetchState.SUCCESS && (
        <>
          <label htmlFor="ltla">Choose a local authority:</label>
          <select
            name="ltla"
            id="ltla"
            value={fetchRegion}
            onChange={handleChange}
          >
            {LtlaList.map((ltla) => (
              <option value={ltla.ltla_code} key={ltla.ltla_code}>
                {ltla.ltla_name}
              </option>
            ))}
          </select>
        </>
      )}
    </div>
  );
};

export default LocationPicker;
