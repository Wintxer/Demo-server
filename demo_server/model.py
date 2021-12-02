from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel
from demo_server.database import Base


class UserBase(BaseModel):
    name: str
    profile_picture: str


class UserCreate(UserBase):
    password: str


class UserDTO(UserBase):
    id: int
    raffles: List["RaffleDTO"] = []
    sheets: List["GoogleSheetDTO"] = []

    class Config:
        orm_mode = True


class GoogleSheetBase(BaseModel):
    url_sheet: str


class GoogleSheetCreate(GoogleSheetBase):
    pass


class GoogleSheetDTO(GoogleSheetBase):
    id_user: int
    id_site: int
    users: List[UserDTO] = []
    sites: List["SiteDTO"] = []


class SiteBase(BaseModel):
    name_site: str
    url_site: str


class SiteCreate(SiteBase):
    pass


class SiteDTO(SiteBase):
    id: str
    raffles: List["RaffleDTO"] = []
    sheets: List[GoogleSheetDTO] = []


class RaffleBase(BaseModel):
    url_raffle: str


class RaffleCreate(RaffleBase):
    pass


class RaffleDTO(RaffleBase):
    id_user: int
    id_site: int
    users: List[UserDTO] = []
    sites: List[SiteDTO] = []


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    profile_picture = Column(String)
    url_sheets = relationship("GoogleSheet", cascade="all, delete-orphan")
    url_raffles = relationship("Raffle", cascade="all, delete-orphan")

    def to_dto(self):
        return UserDTO(
            id=self.id,
            name=self.name,
            profile_picture=self.profile_picture,
            sheets=[sheet.to_dto() for sheet in self.url_sheets],
            raffles=[raffle.to_dto() for raffle in self.url_raffles]
        )


class GoogleSheet(Base):
    __tablename__ = "google_sheet"

    id_user = Column(Integer, ForeignKey('user.id'), primary_key=True)
    id_site = Column(Integer, ForeignKey('site.id'), primary_key=True)
    url_sheet = Column(String)
    users = relationship("User")
    sites = relationship("Site")

    def to_dto(self):
        return GoogleSheetDTO(
            id_user=self.id_user,
            id_site=self.id_site,
            url_sheet=self.url_sheet,
            users=[user.to_dto() for user in self.users],
            sites=[site.to_dto() for site in self.sites]
        )


class Site(Base):
    __tablename__ = "site"

    id = Column(Integer, primary_key=True)
    name_site = Column(String)
    url_site = Column(String)
    url_raffles = relationship("Raffle", cascade="all, delete-orphan")
    url_sheets = relationship("GoogleSheet", cascade="all, delete-orphan")

    def to_dto(self):
        return SiteDTO(
            id=self.id,
            name_site=self.name_site,
            url_site=self.url_site,
            raffles=[raffle.to_dto() for raffle in self.url_raffles],
            sheets=[sheet.to_dto() for sheet in self.url_raffles]
        )


class Raffle(Base):
    __tablename__ = "raffle"

    id_site = Column(Integer, ForeignKey('site.id'), primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'), primary_key=True)
    url_raffle = Column(String)
    users = relationship("User")
    sites = relationship("Site")

    def to_dto(self):
        return RaffleDTO(
            id_site=self.id_site,
            id_user=self.id_user,
            url_raffle=self.url_raffle,
            users=[user.to_dto() for user in self.users],
            sites=[site.to_dto() for site in self.sites]
        )
