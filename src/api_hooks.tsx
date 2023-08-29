import axios from "axios";
import { useState } from "react";
import { FetchState, PostData } from "./types";

export function useGetPosts() {
  const [fetchState, setFetchState] = useState(FetchState.DEFAULT);
  const [posts, setPosts] = useState<Array<PostData>>([]);
  const getPosts = async () => {
    try {
      setFetchState(FetchState.LOADING);

      const res = await axios.get("http://127.0.0.1:105/sample/");
      const resData = res.data as Array<PostData>;

      setPosts(resData);
      setFetchState(FetchState.SUCCESS);
    } catch (err) {
      setFetchState(FetchState.ERROR);
    }
  };

  return [posts, fetchState, getPosts] as const;
}
