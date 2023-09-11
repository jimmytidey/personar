import { PostData } from "../types";
import styled from "styled-components";

const PersonaCardDiv = styled.div`
  width: 20em;
  border: 1px solid black;
  margin: 2em;
`;

const PersonaCardImg = styled.img`
  width: 20em;
  border: 1px solid black;
`;

interface Props {
  key: number;
  postProps: PostData;
}

const PersonarCard = ({ postProps }: Props) => {
  const headshot_url =
    "http://localhost:5173/api/data/headshots/images/" +
    postProps["headshot_file"];
  return (
    <PersonaCardDiv>
      <PersonaCardImg src={headshot_url} />
      <p>Location: {postProps["ltla_name"]}</p>
      <p>Gender: {postProps["sex"]}</p>
      <p>Age: {postProps["age"]}</p>
      <p>Ethnicity: {postProps["ethnicity"]}</p>
      <p>Employment: {postProps["employment"]}</p>
    </PersonaCardDiv>
  );
};

export default PersonarCard;
