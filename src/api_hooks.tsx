import axios from "axios";
import { useState } from "react";
import { FetchState, LtlaListData } from "./types";

export function useGetLtlaListData() {
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

  return [LtlaList, fetchState, getLtlaList] as const;
}
