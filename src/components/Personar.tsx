import PersonarCards from "./PersonarCards";
import LocationPicker from "./LocationPicker";
import { useState } from "react";

const Personar = () => {
  const [fetchRegion, setRegion] = useState("E07000223");
  return (
    <>
      <LocationPicker
        fetchRegion={fetchRegion}
        setRegion={setRegion}
      ></LocationPicker>

      <PersonarCards fetchRegion={fetchRegion}></PersonarCards>
    </>
  );
};

export default Personar;
