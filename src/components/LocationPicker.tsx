import { useGetLtlaListData } from "../api_hooks";
import { FetchState } from "../types";
import { useEffect } from "react";

interface Props {
  fetchRegion: string;
  setRegion: Function;
}

const LocationPicker = ({ fetchRegion, setRegion }: Props) => {
  useEffect(() => {
    getLtlaList();
  }, []);

  const [LtlaList, fetchState, getLtlaList] = useGetLtlaListData();

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
