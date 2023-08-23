import React from "react";
import styled from "styled-components";

const PersonaCardStyles = styled.div`
  width: 20em;
  height: 20em;
  border: 1px solid black;
  margin: 2em;
`;

const Persona = () => {
  return (
    <PersonaCardStyles>
      <h2>Persona</h2>
    </PersonaCardStyles>
  );
};

export default Persona;
