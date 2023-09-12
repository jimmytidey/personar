import styled from "styled-components";
import { PersonasData } from "../types";

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
  postProps: PersonasData;
}

const PersonarCard = ({ postProps }: Props) => {
  const headshot_url =
    import.meta.env.VITE_API_PATH +
    "/headshots/images/" +
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
