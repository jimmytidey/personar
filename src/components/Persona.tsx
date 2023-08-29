import React from "react";
import { useGetPosts } from "../api_hooks";
import { FetchState } from "../types";
import PersonarCard from "./PersonarCard";

const Persona = () => {
  const [posts, fetchState, getPosts] = useGetPosts();

  return (
    <>
      <h1>Personar</h1>
      <div>
        {fetchState === FetchState.DEFAULT && (
          <>
            <p>Fetch personars</p>
            <button onClick={getPosts}>Get Posts</button>
          </>
        )}
        {fetchState === FetchState.LOADING && <p>Fetching posts...</p>}
        {fetchState === FetchState.ERROR && (
          <>
            <p>Oops! Something went wrong. Please try again.</p>
            <button onClick={getPosts}>Get Posts</button>
          </>
        )}
        {fetchState === FetchState.SUCCESS && (
          <>
            <div className="container">
              {posts.map((post, index) => (
                <PersonarCard key={index} postProps={post}></PersonarCard>
              ))}
            </div>
          </>
        )}
      </div>
    </>
  );
};

export default Persona;
